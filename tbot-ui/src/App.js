import './App.css';
import { Home, Navbar} from './components'
import { TradesTable, MarketsTable, OrdersTable, CurrenciesTable,
		 AccountsTable, ExchangesTable } from './components/Tables'
import StrategyExecutionsTable from './components/Strategy.jsx'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  	return (
		<div>
			<Router>
				<Navbar />
				<Switch>
					<Route exact path='/' component={Home} />
					<Route path='/trades' component={TradesTable} />
					<Route path='/markets' component={MarketsTable} />
					<Route path='/orders' component={OrdersTable} />
					<Route path='/currencies' component={CurrenciesTable} />
					<Route path='/accounts' component={AccountsTable} />
					<Route path='/exchanges' component={ExchangesTable} />
					<Route path='/strategy/executions' 
							component={StrategyExecutionsTable} />
				</Switch>
			</Router>
		</div>
	);
}
export default App;
