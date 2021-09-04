import BasicTable from './BasicTable'
import { Table, Collapse } from 'react-bootstrap'

import { React, useState, useEffect } from 'react'

const TradesEndpoint = "http://localhost:8000/trades/";
const CurrenciesEndpoint = "http://localhost:8000/currencies/";
const OrdersEndpoint = "http://localhost:8000/orders/";
const MarketsEndpoint = "http://localhost:8000/markets/";
const AccountsEndpoint = "http://localhost:8000/accounts/";
const ExchangesEndpoint = "http://localhost:8000/exchanges/";
const StrategiesEndpoint = "http://localhost:8000/strategies/";
const StrategyExecutionsEndpoint = "http://localhost:8000/strategy/executions/";

const TradesTable = () => {
	return <BasicTable endpoint={TradesEndpoint} />;
}

const CurrenciesTable = () => {
	return <BasicTable endpoint={CurrenciesEndpoint} />;
}

const OrdersTable = () => {
	return <BasicTable endpoint={OrdersEndpoint} />;
}

const MarketsTable = () => {
	return <BasicTable endpoint={MarketsEndpoint} />;
}

const AccountsTable = () => {
	return <BasicTable endpoint={AccountsEndpoint} />;
}

const ExchangesTable = () => {
	return <BasicTable endpoint={ExchangesEndpoint} />;
}

export { TradesTable, CurrenciesTable, OrdersTable, 
	     MarketsTable, AccountsTable, ExchangesTable,};
