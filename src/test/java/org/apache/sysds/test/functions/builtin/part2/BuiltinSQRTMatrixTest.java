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

	private final static double eps = 1e-8;

	@Override
	public void setUp() {
		addTestConfiguration(TEST_NAME, new TestConfiguration(TEST_CLASS_DIR, TEST_NAME, new String[] {"C"}));
	}

/*
	// tests for strategy "COMMON"
	@Test
	public void testSQRTMatrixJavaSize1x1() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 1);
	}

	@Test
	public void testSQRTMatrixJavaUpperTriangularMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 2);
	}

	@Test
	public void testSQRTMatrixJavaDiagonalMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 3);
	}

	@Test
	public void testSQRTMatrixJavaPSDMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 4);
	}

	@Test
	public void testSQRTMatrixJavaPSDMatrixSize3x3() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 5);
	}

	@Test
	public void testSQRTMatrixJavaPSDMatrixSize4x4() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 6);
	}

	@Test
	public void testSQRTMatrixJavaPSDMatrixSize8x8() {
		runSQRTMatrix(true, ExecType.CP, "COMMON", 7);
	}
*/

	// tests for strategy "DML"

	@Test
	public void testSQRTMatrixDMLSize1x1() {
		runSQRTMatrix(true, ExecType.CP, "DML", 1);
	}

	@Test
	public void testSQRTMatrixDMLUpperTriangularMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "DML", 2);
	}

	@Test
	public void testSQRTMatrixDMLDiagonalMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "DML", 3);
	}

	@Test
	public void testSQRTMatrixDMLPSDMatrixSize2x2() {
		runSQRTMatrix(true, ExecType.CP, "DML", 4);
	}

	@Test
	public void testSQRTMatrixDMLPSDMatrixSize3x3() {
		runSQRTMatrix(true, ExecType.CP, "DML", 5);
	}

	@Test
	public void testSQRTMatrixDMLPSDMatrixSize4x4() {
		runSQRTMatrix(true, ExecType.CP, "DML", 6);
	}

	@Test
	public void testSQRTMatrixDMLPSDMatrixSize8x8() {
		runSQRTMatrix(true, ExecType.CP, "DML", 7);
	}


	private void runSQRTMatrix(boolean defaultProb, ExecType instType, String strategy, int test_case) {
		Types.ExecMode platformOld = setExecMode(instType);
		try {
			loadTestConfiguration(getTestConfiguration(TEST_NAME));

			// find path to associated dml script and define parameters
			String HOME = SCRIPT_DIR + TEST_DIR;
			fullDMLScriptName = HOME + TEST_NAME + ".dml";
			programArgs = new String[] {"-args", input("X"), strategy, output("Y")};

			// define input matrix for the matrix sqrt function according to test case
			double[][] X = null;
			switch(test_case) {
				case 1: // arbitrary square matrix of dimension 1x1 (PSD)
					double[][] X1 = {
							{4}
					};
					X = X1;
					break;
				case 2: // arbitrary upper right triangular matrix (PSD) of dimension 2x2
					double[][] X2 = {
							{1, 1},
							{0, 1},
					};
					X = X2;
					break;
				case 3: // arbitrary diagonal matrix (PSD) of dimension 2x2
					double[][] X3 = {
							{1, 0},
							{0, 1},
					};
					X = X3;
					break;
				case 4: // arbitrary PSD matrix of dimension 2x2
					// PSD matrix generated by taking (A^T)A of matrix A = [[1, 0], [2, 3]]
					double[][] X4 = {
							{1, 2},
							{2, 13}
					};
					X = X4;
					break;
				case 5: // arbitrary PSD matrix of dimension 3x3
					// PSD matrix generated by taking (A^T)A of matrix A =
					// [[1.5, 0, 1.2],
					// [2.2, 3.8, 4.4],
					// [4.2, 6.1, 0.2]]
					double[][] X5 = {
							{3.69, 8.58, 6.54},
							{8.58, 38.64, 33.30},
							{6.54, 33.3, 54.89}
					};
					X = X5;
					break;
				case 6: // arbitrary PSD matrix of dimension 4x4
					// PSD matrix generated by taking (A^T)A of matrix A=
					// [[1, 0, 5, 6],
					//  [2, 3, 0, 2],
					//  [5, 0, 1, 1],
					//  [2, 3, 4, 8]]
					double[][] X6 = {
							{62, 14, 16, 70},
							{14, 17, 12, 29},
							{16, 12, 27, 22},
							{70, 29, 22, 93}
					};
					X = X6;
					break;
				case 7: // arbitrary PSD matrix of dimension 8x8
					// PSD matrix generated by taking (A^T)A of matrix A =
					// [[ 8.41557894,  3.44748042,  1.44911908,  4.95381036,  4.42875187,   4.14710712, -0.42719386,  6.1366026 ],
					// [ 3.44748042, 11.38083039,  4.99475137,  3.36734826,  4.08943809,   4.23308448,  4.50030176,  3.92552912],
					// [ 1.44911908,  4.99475137,  9.78651357,  4.00347878,  4.60244914,   4.24468227,  3.62945751,  6.54033601],
					// [ 4.95381036,  3.36734826,  4.00347878, 12.75936071,  3.78643598,   1.99998784,  5.41689723,  7.9756991 ],
					// [ 4.42875187,  4.08943809,  4.60244914,  3.78643598, 12.49158813,   6.69560056,  3.87176913,  5.5028702 ],
					// [ 4.14710712,  4.23308448,  4.24468227,  1.99998784,  6.69560056,   7.66015758,  4.21792513,  4.53489207],
					// [-0.42719386,  4.50030176,  3.62945751,  5.41689723,  3.87176913,   4.21792513,  9.07079513,  2.64352781],
					// [ 6.1366026 ,  3.92552912,  6.54033601,  7.9756991 ,  5.5028702 ,   4.53489207,  2.64352781,  8.92801728]]
					double[][] X7 = {
							{184, 150, 140, 194, 192, 153,  91, 211},
							{150, 248, 203, 198, 216, 187, 171, 214},
							{140, 203, 234, 212, 223, 185, 165, 237},
							{194, 198, 212, 326, 228, 177, 190, 287},
							{192, 216, 223, 228, 318, 239, 180, 262},
							{153, 187, 185, 177, 239, 199, 152, 209},
							{ 91, 171, 165, 190, 180, 152, 185, 170},
							{211, 214, 237, 287, 262, 209, 170, 297}
					};
					X = X7;
					break;
			}

			assert X != null;

			// write the input matrix and strategy for matrix sqrt function to dml script
            writeInputMatrixWithMTD("X", X, true);

			// run the test dml script
			runTest(true, false, null, -1);

			// read the result matrix from the dml script output Y
			HashMap<MatrixValue.CellIndex, Double> actual_Y = readDMLMatrixFromOutputDir("Y");

			//System.out.println("This is the actual Y: " + actual_Y);

			// create a HashMap with Matrix Values from the input matrix X to compare to the received output matrix
			HashMap<MatrixValue.CellIndex, Double> expected_Y = new HashMap<>();
			for (int r = 0; r < X.length; r++) {
				for (int c = 0; c < X[0].length; c++) {
					expected_Y.put(new MatrixValue.CellIndex(r + 1, c + 1), X[r][c]);
				}
			}

			// compare the expected matrix (the input matrix X) with the received output matrix Y, which should be the (SQRT_MATRIX(X))^2 = X again
			TestUtils.compareMatrices(expected_Y, actual_Y, eps, "Expected-DML", "Actual-DML");
		}
		finally {
			resetExecMode(platformOld);
		}
	}
}
