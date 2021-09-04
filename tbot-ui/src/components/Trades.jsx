import React, { useState, useEffect } from 'react';


const TradeRow = (props) => {

	return (
		<tr>
			<td>{props.tradeId}</td>
			<td>{props.timestamp}</td>
			<td>{props.takerMaker}</td>
			<td>{props.amount}</td>
			<td>{props.feeCurrency}</td>
			<td>{props.feeCost}</td>
			<td>{props.feeRate}</td>
		</tr>
	)
}

const TradeTable = (props) => {
	const [trades, setTrades] = useState([])

	const fetchTrades = () => {
		fetch("http://localhost:8000/trades/")
			.then(res=>res.json())
			.then((result) => {
				console.log(result);
				setTrades(result);
			},
			(error) => {
				console.log(error);
			});
			
	}

	useEffect(() => {
		fetchTrades();
	}, []);
	
	return (
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Timestamp</th>
					<th>T/M</th>
					<th>Amount</th>
					<th>Currency</th>
					<th>Cost</th>
					<th>Rate</th>
				</tr>
			</thead>
			<tbody>	
				{ trades.map((trade) => <TradeRow key={trade.trade_id} 
					tradeId={trade.trade_id}
					timestamp={trade.timestamp} amount={trade.amount}
					feeCurrency={trade.fee_currency} feeCost={trade.fee_cost}
					feeRate={trade.fee_rate} takerMaker={trade.taker_or_maker} />)  }
			</tbody>
			
		</table>
	)
}

export default TradeTable;
