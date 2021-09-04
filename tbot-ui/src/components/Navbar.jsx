import React from 'react'
import { Navbar, Nav, Container } from 'react-bootstrap'

const navbar = (props) => {
	var buttons = []

	return (
		<Navbar bg="dark" varient="dark">
			<Container>
			<Nav>
				<Nav.Link href="/">Home</Nav.Link>
				<Nav.Link href="/trades">Trades</Nav.Link>
				<Nav.Link href="/markets">Markets</Nav.Link>
				<Nav.Link href="/orders">Orders</Nav.Link>
				<Nav.Link href="/accounts">Accounts</Nav.Link>
				<Nav.Link href="/exchanges">Exchanges</Nav.Link>
				<Nav.Link href="/currencies">Currencies</Nav.Link>
				<Nav.Link href="/strategy/executions">Executions</Nav.Link>
			</Nav>
			</Container>
		</Navbar>
			
	)
}

export default navbar
