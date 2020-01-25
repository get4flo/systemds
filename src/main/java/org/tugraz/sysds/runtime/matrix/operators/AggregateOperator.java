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


package org.tugraz.sysds.runtime.matrix.operators;

import java.io.Serializable;

import org.tugraz.sysds.common.Types.CorrectionLocationType;
import org.tugraz.sysds.runtime.functionobjects.KahanPlus;
import org.tugraz.sysds.runtime.functionobjects.KahanPlusSq;
import org.tugraz.sysds.runtime.functionobjects.Minus;
import org.tugraz.sysds.runtime.functionobjects.Or;
import org.tugraz.sysds.runtime.functionobjects.Plus;
import org.tugraz.sysds.runtime.functionobjects.ValueFunction;


public class AggregateOperator  extends Operator implements Serializable
{
	private static final long serialVersionUID = 8761527329665129670L;

	public final double initialValue;
	public final BinaryOperator increOp;
	public final CorrectionLocationType correction;
	
	public AggregateOperator(double initValue, ValueFunction op) {
		this(initValue, op, CorrectionLocationType.INVALID);
	}
	
	public AggregateOperator(double initValue, ValueFunction op, CorrectionLocationType correctionLocation) {
		//as long as (v op 0)=v, then op is sparseSafe
		super(op instanceof Plus || op instanceof KahanPlus || op instanceof KahanPlusSq 
			|| op instanceof Or || op instanceof Minus);
		initialValue = initValue;
		increOp = new BinaryOperator(op);
		correction = correctionLocation;
	}
	
	public boolean existsCorrection() {
		return correction != CorrectionLocationType.NONE;
	}
}
