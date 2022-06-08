# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

import json
import os
import re
import sys
import traceback
from parser import FunctionParser
from typing import List, Tuple


class PythonAPIFileGenerator(object):

    target_path = os.path.join(os.path.dirname(os.path.dirname(
        __file__)), 'systemds', 'operator', 'algorithm', 'builtin')
    licence_path = os.path.join('resources', 'template_python_script_license')
    template_path = os.path.join('resources', 'template_python_script_imports')

    source_path: str
    licence: str
    imports: str
    generated_by: str
    generated_from: str

    init_path = os.path.join(os.path.dirname(os.path.dirname(
        __file__)), 'systemds', 'operator', 'algorithm', '__init__.py')
    init_import = u"from .builtin.{function} import {function} \n"
    init_all = u"__all__ = {functions} \n"

    def __init__(self, source_path: str, extension: str = 'py'):
        super(PythonAPIFileGenerator, self).__init__()
        self.source_path = source_path

        self.extension = '.{extension}'.format(extension=extension)
        os.makedirs(self.__class__.target_path, exist_ok=True)
        self.function_names = list()
        path = os.path.dirname(__file__)

        with open(os.path.join(path, self.__class__.template_path), 'r') as f:
            self.imports = f.read()
        with open(os.path.join(path, self.__class__.licence_path), 'r') as f:
            self.licence = f.read()

        self.generated_by = "# Autogenerated By   : src/main/python/generator/generator.py\n"
        self.generated_from = "# Autogenerated From : "

    def generate_file(self, filename: str, file_content: str, dml_file: str):
        """
        Generates file in self.path with name file_name
        and given file_contents as content
        """
        path = os.path.dirname(__file__)

        target_file = os.path.join(self.target_path, filename) + self.extension
        with open(target_file, "w") as new_script:
            new_script.write(self.licence)
            new_script.write(self.generated_by)
            new_script.write((self.generated_from + dml_file + "\n").replace(
                "../", "").replace("src/main/python/generator/", ""))
            new_script.write(self.imports)
            new_script.write(file_content)

        self.function_names.append(filename)

    def generate_init_file(self):
        with open(self.init_path, "w") as init_file:
            init_file.write(self.licence)
            init_file.write(self.generated_by)
            init_file.write("\n")
            for f in self.function_names:
                init_file.write(self.init_import.format(function=f))
            init_file.write("\n")
            init_file.write(self.init_all.format(
                functions=self.function_names).replace(",", ",\n"))


class PythonAPIFunctionGenerator(object):

    api_template = u"""def {function_name}({parameters}):
    {header}
    {params_dict}
    {api_call}\n"""

    kwargs_parameter_string = u"**kwargs: Dict[str, VALID_INPUT_TYPES]"
    kwargs_result = u"params_dict.update(kwargs)"

    type_mapping_file = os.path.join('resources', 'type_mapping.json')

    type_mapping_pattern = r"^([^\[\s]+)"

    path = os.path.dirname(__file__)
    type_mapping_path = os.path.join(path, type_mapping_file)

    with open(type_mapping_path, 'r') as mapping:
        type_mapping = json.load(mapping)

    def __init__(self):
        super(PythonAPIFunctionGenerator, self).__init__()

    def generate_function(self, data: dict) -> str:
        """
        Generates function definition for PythonAPI
        @param data:
            {
                'function_name': 'some_name',
                'function_header': 'header contained in \"\"\"'
                'parameters': [('param1','type','default_value'), ...],
                'return_values': [('retval1', 'type'),...]
            }
        @return: function definition
        """
        function_name = data['function_name']
        parameters = self.format_param_string(
            data['parameters'], len(function_name))
        header = data['function_header'] if data['function_header'] else ""
        params_dict = self.format_params_dict_string(data['parameters'])
        api_call = self.format_api_call(
            data['parameters'],
            data['return_values'],
            data['function_name']
        )
        return self.__class__.api_template.format(
            function_name=function_name, parameters=parameters, header=header,
            params_dict=params_dict, api_call=api_call)

    def replace_types(self,  item: str):
        pattern = self.__class__.type_mapping_pattern
        return self.__class__.type_mapping["type"].get(re.search(pattern, str(
            item).lower()).group() if item else item.lower(), item)

    def format_param_string(self, parameters: List[Tuple[str]], nameLength: int) -> str:
        try:
            result = []
            has_optional = False
            path = os.path.dirname(__file__)
            newline_spacing = "\n" + " " * (nameLength + 5)

            for param in parameters:
         
                param[1] = self.replace_types(param[1])
    
                if "[" in param[1] or "[" in param[0]:
                    raise AttributeError(
                        "Failed parsing param" + str(param) + "\n" + str(parameters))
                if param[2] is not None:
                    has_optional = True
               
                else:
                    result.append("{nl}{name}: {typ},".format(
                        result=result, name=param[0], typ=param[1],
                        nl=newline_spacing))
            if len(result) == 0:
                result = ""
            else:
                result[0] = result[0][len(newline_spacing):]
                result[-1] = result[-1][:-1]
                result = "".join(result)
                if has_optional:
                    result = u"{result},{nl}{kwargs}".format(
                        result=result, kwargs=self.__class__.kwargs_parameter_string,
                        nl=newline_spacing)

            return result
        except Exception as e:
            raise AttributeError("Failed Formatting parameter strings: " +
                                 str(parameters) + " " + format_exception(e))

    def format_params_dict_string(self, parameters: List[Tuple[str]]) -> str:
        if not len(parameters):
            return ""
        has_optional = False
        result = ""
        for param in parameters:
            if param[2] is not None:
                has_optional = True
            else:
                if len(result):
                    result = u"{result}, ".format(
                        result=result)
                else:
                    result = u"params_dict = {"
                result = u"{result}\'{name}\': {name}".format(
                    result=result,
                    name=param[0]
                )
        result = u"{result}}}".format(result=result)
        if has_optional:
            result = u"{result}\n    {kwargs}".format(
                result=result,
                kwargs=self.__class__.kwargs_result
            )
        return result

    def format_api_call(self,
                        parameters: List[Tuple[str]],
                        return_values: List[Tuple[str]],
                        function_name: str
                        ) -> str:
        length = len(return_values)
        param_string = ""
        param = parameters[0]
        sds_context = "{param}.sds_context".format(param=param[0])
        pattern = r"^[^\[]+"
        if length > 1:
            output_nodes_str, op_assignments = self.generate_output_nodes(
                return_values, pattern, sds_context)
            multi_return_str = self.generate_multireturn(
                sds_context, function_name)
            result = "\n{out_nodes}\n\n{multi_return}\n\n{op_assign}\n\n    return op".format(
                out_nodes=output_nodes_str,
                multi_return=multi_return_str,
                op_assign=op_assignments
            )
            return result
        else:
            value = return_values[0]
            output_type = re.search(pattern, value[1])
            if(output_type):
                output_type = output_type[0].upper()
            else:
                raise AttributeError("Error in pattern match: " + str(value) + "\n" +
                                     function_name + "\n" + str(parameters) + "\n" + str(return_values))
            result = ("{sds_context}," +
                      "\n        \'{function_name}\'," +
                      "\n        named_input_nodes=params_dict").format(
                sds_context=sds_context,
                function_name=function_name
            )
            result = "return Matrix({params})".format(params=result)
            return result

    def generate_output_nodes(self, return_values, pattern, sds_context):
        lines = []
        op_assignment = []
        output_nodes = "\n    output_nodes = ["
        for idx, value in enumerate(return_values):
            output_type = re.search(pattern, value[1])[0].upper()

            output_type = output_type.lower()

            if output_type == "matrix":
                object_type = "Matrix"
            elif output_type == "frame":
                object_type = "Frame"
            elif output_type == "double":
                object_type = "Scalar"
            elif output_type == "boolean":
                object_type = "Scalar"
            elif output_type == "integer":
                object_type = "Scalar"
            elif output_type == "list":
                object_type = "List"
            else:
                raise ValueError("Unknown type " + object_type)

            lines.append("    vX_{idx} = {obj}({sds}, '')".format(
                idx=idx, obj=object_type, sds=sds_context))
            output_nodes += "vX_{idx}, ".format(idx=idx)
            op_assignment.append(
                "    vX_{idx}._unnamed_input_nodes = [op]".format(idx=idx))
        output_nodes += "]"
        lines = "\n".join(lines) + output_nodes
        op_assignment = "\n".join(op_assignment)
        return lines, op_assignment

    def generate_multireturn(self, sds_context, function_name):
        return ("    op = MultiReturn({sds}, \'{function_name}\', output_nodes," +
                " named_input_nodes=params_dict)").format(
            sds=sds_context, function_name=function_name)


class PythonAPIDocumentationGenerator(object):

    param_str = "\n    :param {pname}: {meaning}"
    return_str = "\n    :return: \'OperationNode\' containing {meaning} \n"

    def __init__(self):
        super(PythonAPIDocumentationGenerator, self).__init__()

    def generate_documentation(self, header_data: dict, data: dict):
        """
        Generates function header for PythonAPI
        @param data:
            {
                'function_name': 'some_name',
                'parameters': [('param1','description'), ...],
                'return_values': [('retval1', 'descritpion'),...]
            }
        @return: function header including '\"\"\"' at start and end
        """
        description = header_data["description"].replace("\n", "\n    ")
        input_param = self.header_parameter_string(header_data["parameters"])
        output_param = self.header_return_string(header_data["return_values"])

        if description == "":
            data['function_header'] = ""
        elif header_data["return_values"] == []:
            data['function_header'] = '"""\n    ' + description + '"""'
        else:
            res_str = "\n    :return: \'OperationNode\' containing {meaning} \n".format(
                meaning=output_param.lower())
            data['function_header'] = '"""\n    ' + description + \
                input_param + res_str + '    """'

    def header_parameter_string(self, parameter: dict) -> str:
        parameter_str = "\n    "
        for param in parameter:
            parameter_str += self.__class__.param_str.format(
                pname=param[0], meaning=param[1])

        return parameter_str

    def header_return_string(self, parameter: dict) -> str:
        meaning_str = "\n        "
        first = True
        for param in parameter:
            if first:
                meaning_str += param[1]
            else:
                meaning_str += "\n        & " + param[1]

        return meaning_str


def format_exception(e):
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(
        sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]

    return exception_str


if __name__ == "__main__":
    if "python" in os.getcwd():
        source_path = os.path.join("../../../", 'scripts', 'builtin')
    else:
        source_path = os.path.join(os.path.dirname(
            __file__), "../../../../", 'scripts', 'builtin')
    file_generator = PythonAPIFileGenerator(source_path)
    fun_generator = PythonAPIFunctionGenerator()
    f_parser = FunctionParser(source_path)
    doc_generator = PythonAPIDocumentationGenerator()
    files = f_parser.files()
    for dml_file in files:
        try:
            header_data = f_parser.parse_header(dml_file)
            data = f_parser.parse_function(dml_file)
            f_parser.check_parameters(header_data, data)
            doc_generator.generate_documentation(header_data, data)

            if data['function_header'] == "":
                print("[WARNING] in : \'{file_name}\' failed parsing docs.".format(
                    file_name=dml_file))

            script_content = fun_generator.generate_function(data)
        except Exception as e:
            print("[ERROR] error in : \'{file_name}\' \n{err} \n{trace}.".format(
                file_name=dml_file, err=e, trace=format_exception(e)))
            continue
        file_generator.generate_file(
            data["function_name"], script_content, dml_file)
    file_generator.generate_init_file()
