import { React, useState, useEffect } from 'react';
import { Table } from 'react-bootstrap';

const getKeys = (data) =>  {
	if (data.length > 0)
		return Object.keys(data[0]);
	else
		return [];
}

const getHeader = (data) => {
	let keys = getKeys(data);
	return  keys.map(key => {
		return <th key={key}>{key}</th>
	});
}

const getRow = (data, keys) => {
	return keys.map((key, index) => {
		return <td key={index}>{data[key]}</td>
	});
}

const getRows = (data) => {
	let keys = getKeys(data);
	return data.map((row, index) => {
		return <tr key={index}>{getRow(row, keys)}</tr>
	});
}

const fetchDataFromEndpoint = (endpoint) => {
	let data = fetch(endpoint)
		.then(res=>res.json())
		.then(res=>{return res});
	return data;
}

const BasicTable = (props) => {
	const [data, setData] = useState([]);
	useEffect(() => {
		if (!('data' in props)) {
			fetchDataFromEndpoint(props.endpoint)
				.then(res => setData(res));
		} else {
			setData(props.data);
		}
	}, []);
	return (
		<div>
			<Table>
				<thead><tr>{getHeader(data)}</tr></thead>
				<tbody>{getRows(data)}</tbody>
			</Table>
		</div>
	)

}

export default BasicTable;
