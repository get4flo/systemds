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

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/km.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def km(X: Matrix,
       TE: Matrix,
       GI: Matrix,
       SI: Matrix,
       **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    Builtin function that implements the analysis of survival data with KAPLAN-MEIER estimates
    
    
    :param X: Input matrix X containing the survival data:
        timestamps, whether event occurred (1) or data is censored (0), and a
        number of factors (categorical features) for grouping and/or stratifying
    :param TE: Column indices of X which contain timestamps (first entry) and event
        information (second entry)
    :param GI: Column indices of X corresponding to the factors to be used for grouping
    :param SI: Column indices of X corresponding to the factors to be used for stratifying
    :param alpha: Parameter to compute 100*(1-alpha)% confidence intervals for the survivor
        function and its median
    :param err_type: "greenwood" Parameter to specify the error type according to "greenwood" (the default) or "peto"
    :param conf_type: Parameter to modify the confidence interval; "plain" keeps the lower and
        upper bound of the confidence interval unmodified, "log" (the default)
        corresponds to logistic transformation and "log-log" corresponds to the
        complementary log-log transformation
    :param test_type: If survival data for multiple groups is available specifies which test to
        perform for comparing survival data across multiple groups: "none" (the default)
        "log-rank" or "wilcoxon" test
    :return: 'OperationNode' containing 
        matrix km whose dimension depends on the number of groups (denoted by g) and
        strata (denoted by s) in the data:
        each collection of 7 consecutive columns in km corresponds to a unique
        combination of groups and strata in the data with the following schema
        1. col: timestamp
        2. col: no. at risk
        3. col: no. of events
        4. col: kaplan-meier estimate of survivor function surv
        5. col: standard error of surv
        6. col: lower 100*(1-alpha)% confidence interval for surv
        7. col: upper 100*(1-alpha)% confidence interval for survmatrix m whose dimension depends on the number of groups (g) and strata (s) in
        the data (k denotes the number of factors used for grouping  ,i.e., ncol(gi) and
        l denotes the number of factors used for stratifying, i.e., ncol(si))
        m[,1:k]: unique combination of values in the k factors used for grouping
        m[,(k+1):(k+l)]: unique combination of values in the l factors used for stratifying
        m[,k+l+1]: total number of records
        m[,k+l+2]: total number of events
        m[,k+l+3]: median of surv
        m[,k+l+4]: lower 100*(1-alpha)% confidence interval of the median of surv
        m[,k+l+5]: upper 100*(1-alpha)% confidence interval of the median of surv
        if the number of groups and strata is equal to 1, m will have 4 columns with
        m[,1]: total number of events
        m[,2]: median of surv
        m[,3]: lower 100*(1-alpha)% confidence interval of the median of surv
        m[,4]: upper 100*(1-alpha)% confidence interval of the median of survif survival data from multiple groups available and ttype=log-rank or wilcoxon,
        a 1 x 4 matrix t and an g x 5 matrix t_groups_oe with
        t_groups_oe[,1] = no. of events
        t_groups_oe[,2] = observed value (o)
        t_groups_oe[,3] = expected value (e)
        t_groups_oe[,4] = (o-e)^2/e
        t_groups_oe[,5] = (o-e)^2/v
        t[1,1] = no. of groups
        t[1,2] = degree of freedom for chi-squared distributed test statistic
        t[1,3] = test statistic
        t[1,4] = p-value 
    """
    params_dict = {'X': X, 'TE': TE, 'GI': GI, 'SI': SI}
    params_dict.update(kwargs)
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    vX_2 = Matrix(X.sds_context, '')
    vX_3 = Matrix(X.sds_context, '')
    output_nodes = [vX_0, vX_1, vX_2, vX_3, ]

    op = MultiReturn(X.sds_context, 'km', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]
    vX_2._unnamed_input_nodes = [op]
    vX_3._unnamed_input_nodes = [op]

    return op
