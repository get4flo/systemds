/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.apache.sysds.test.functions.builtin.part2;

import org.apache.sysds.common.Types;
import org.apache.sysds.common.Types.ExecType;
import org.apache.sysds.runtime.matrix.data.MatrixValue;
import org.apache.sysds.test.AutomatedTestBase;
import org.apache.sysds.test.TestConfiguration;
import org.apache.sysds.test.TestUtils;
import org.junit.Test;

import java.util.HashMap;

public class BuiltinSQRTMatrixTest extends AutomatedTestBase {
	private final static String TEST_NAME = "SQRTMatrix";
	private final static String TEST_DIR = "functions/builtin/";
	private static final String TEST_CLASS_DIR = TEST_DIR + BuiltinSQRTMatrixTest.class.getSimpleName() + "/";

	private final static double eps = 1e-10;

	@Override
	public void setUp() {
		addTestConfiguration(TEST_NAME, new TestConfiguration(TEST_CLASS_DIR, TEST_NAME, new String[] {"C"}));
	}

	// tests for strategy "COMMON"
	@Test
	public void testSQRTMatrix() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 1);
	}

	/* TODO: add more test cases for COMMON and then for other strategies
	@Test
	public void testSQRTMatrix() {

	}
	 */

	private void runSQRTMatrix(boolean defaultProb, ExecType instType, String strategy, int test_case) {
		Types.ExecMode platformOld = setExecMode(instType);
		try {
			loadTestConfiguration(getTestConfiguration(TEST_NAME));

			// find path to associated dml script and define parameters
			String HOME = SCRIPT_DIR + TEST_DIR;
			fullDMLScriptName = HOME + TEST_NAME + ".dml";
			programArgs = new String[] {"-args", input("X"), input("S"), output("Y"), output("R")};

			// define input matrix for the matrix sqrt function according to test case
			double[][] X = null;
			switch(test_case) {
				case 1:
					double[][] X1 = {
							{3, 1, 2, 1, 5},
							{2, 1, 2, 2, 4},
							{1, 1, 1, 3, 3},
							{4, 2, 1, 4, 2},
							{2, 2, 1, 5, 1},};
					X = X1;
					break;
				case 2:
					double[][] X2 = { // TODO: change values
							{3, 1, 2, 1, 5},
							{2, 1, 2, 2, 4},
							{1, 1, 1, 3, 3},
							{4, 2, 1, 4, 2},
							{2, 2, 1, 5, 1},};
					X = X2;
					break;
					// TODO: add more test cases
			}

			assert X != null;

			// write the input matrix and strategy for matrix sqrt function to dml script
            writeInputMatrixWithMTD("X", X, true);
			writeInputMatrixWithMTD("S", strategy, true); // TODO: find how to write a string to dml

			// run the test dml script
			runTest(true, false, null, -1);

			// read the result matrix from the dml script output Y
			HashMap<MatrixValue.CellIndex, Double> actual_Y = readDMLMatrixFromOutputDir("Y");

			// create a HashMap with Matrix Values from the input matrix X to compare to the received output matrix
			HashMap<MatrixValue.CellIndex, Double> expected_Y = new HashMap<>();
			for (int r = 0; r < X.length; r++) {
				for (int c = 0; c < X[0].length; c++) {
					expected_Y.put(new MatrixValue.CellIndex(r, c), X[r][c]);
				}
			}

			// compare the expected matrix (the input matrix X) with the received output matrix Y, which should be the (SQRT_MATRIX(X))^2 = X again
			TestUtils.compareMatrices(expected_Y, actual_Y, eps, "Expected-DML", "Actual-DML");

			// read the result accuracy from the dml script output R
			HashMap<MatrixValue.CellIndex, Double> accuracy = readDMLScalarFromOutputDir("R");
			System.out.println(accuracy.toString());
		}
		finally {
			resetExecMode(platformOld);
		}
	}
}
