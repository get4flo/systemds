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
# Autogenerated From : scripts/builtin/shortestPath.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def shortestPath(G: Matrix,
                 sourceNode: int,
                 **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    Computes the minimum distances (shortest-path) between a single source vertex and every other vertex in the graph.
    
    Grzegorz Malewicz, Matthew H. Austern, Aart J. C. Bilk, 
    James C. Dehnert, Ikkan Horn, Naty Leiser and Grzegorz Czajkowski:
    Pregel: A System for Large-Scale Graph Processing, SIGMOD 2010
    
    
    :param G: adjacency matrix of the labeled graph: Such graph can be directed
        (G is symmetric) or undirected (G is not symmetric).
        The values of G can be 0/1 (just specifying whether the nodes
        are connected or not) or integer values (representing the weight
        of the edges or the distances between nodes, 0 if not connected).
    :param maxi: Integer max number of iterations accepted (0 for FALSE, i.e.
        max number of iterations not defined)
    :param sourceNode: node index to calculate the shortest paths to all other nodes.
    :param verbose: flag for verbose debug output
    :return: 'OperationNode' containing 
        output matrix (double) of minimum distances (shortest-path) between
        vertices: the value of the ith row and the jth column of the output
        matrix is the minimum distance shortest-path from vertex i to vertex j.
        when the value of the minimum distance is infinity, the two nodes are
        not connected. 
    """
    params_dict = {'G': G, 'sourceNode': sourceNode}
    params_dict.update(kwargs)
    return Matrix(G.sds_context,
        'shortestPath',
        named_input_nodes=params_dict)
