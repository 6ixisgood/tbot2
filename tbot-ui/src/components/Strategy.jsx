import React, { useState, useEffect } from 'react';
import { Table, Collapse } from 'react-bootstrap';
import BasicTable from './BasicTable';

const AnalysisRows = (props) => {
	let data = props.data
	return (
		<>
			<tr>
				<td>1</td>
				<td>{data.execution.order_1.market}</td>
				<td>{data.execution.order_1.side}</td>
				<td>{data.execution.order_1.price}</td>
				<td>{data.execution.order_1.amount}</td>
				<td>{data.execution.order_1.price*data.execution.order_1.amount}</td>
				<td>{data.o1_price_d}</td>
				<td>{data.o1_amount_d}</td>
				<td>Cost Diff</td>
			</tr>
			<tr>
				<td>2</td>
				<td>{data.execution.order_2.market}</td>
				<td>{data.execution.order_2.side}</td>
				<td>{data.execution.order_2.price}</td>
				<td>{data.execution.order_2.amount}</td>
				<td>{data.execution.order_2.price*data.execution.order_2.amount}</td>
				<td>{data.o2_price_d}</td>
				<td>{data.o2_amount_d}</td>
				<td>Cost Diff</td>
			</tr>
			<tr>
				<td>3</td>
				<td>{data.execution.order_3.market}</td>
				<td>{data.execution.order_3.side}</td>
				<td>{data.execution.order_3.price}</td>
				<td>{data.execution.order_3.amount}</td>
				<td>{data.execution.order_3.price*data.execution.order_3.amount}</td>
				<td>{data.o3_price_d}</td>
				<td>{data.o3_amount_d}</td>
				<td>Cost Diff</td>
			</tr>
		</>
	)
	
}

const AnalysisTable = (props) => {
	let data = props.data;
	return (
		<Table>
			<thead>
				<tr>
					<th>Order</th>
					<th>Market</th>
					<th>Side</th>
					<th>Price</th>
					<th>Amount</th>
					<th>Cost</th>
					<th>$ &Delta;</th>
					<th>A &Delta;</th>
				</tr>
			</thead>
			<tbody><AnalysisRows data={data}/></tbody>
		</Table>

	)
}

const getCurrencyFromSide = (symbol, side) => {
	let split = symbol.split('/')
	return (side === 'buy') ? split[0] : split[1];
		
}

const StrategyExecutionRow = (props) => {
	// useState for collapse controls
	const [open, setOpen] = useState(false);
	const [collapsed, setCollapsed] = useState(true);

	let data = props.data
	return (
		<>
			<tr key={data.url} onClick={() => setOpen(!open)}>
				<td style={{float:"left"}}>{(collapsed) ? '+' : '-'}</td>
				<td>{data.execution.strategy}</td>
				<td>{data.execution.timestamp}</td>
				<td>{getCurrencyFromSide(data.execution.order_1.market)}</td>
				<td>{getCurrencyFromSide(data.execution.order_2.market)}</td>
				<td>{getCurrencyFromSide(data.execution.order_3.market)}</td>
				<td>{data.payoff}</td>
			</tr>
			<Collapse in={open} onEntering={() => setCollapsed(false)}
						  onExited={() => setCollapsed(true)}>
				<tr>
						<td colSpan="3">
						</td>
						<td colSpan="4">
							<AnalysisTable data={data} />

						</td>
				</tr>
			</Collapse>		
		</>
	)
}

const StrategyRows = (props) => {
	let data = props.data;
	return data.map((row, index) => {
		return <StrategyExecutionRow key={index} data={row} />
	});
}

const StrategyExecutionsTable = () => {

	const [data, setData] = useState([]);

	useEffect(() => {
		fetch('http://localhost:8000/strategy/analysis/')
			.then(res=>res.json())
			.then(res=>setData(res))
	}, []);


	return (
		<div>
			<Table> 
				<thead>
					<tr>
						<th></th>
						<th>Strategy</th>
						<th>Timestamp</th>
						<th>Currency 1</th>
						<th>Currency 2</th>
						<th>Currency 3</th>
						<th>+/-</th>
					</tr>
				</thead>
				<tbody><StrategyRows data={data} /></tbody>
			</Table>
		</div>
					
	)

}



export default StrategyExecutionsTable;
