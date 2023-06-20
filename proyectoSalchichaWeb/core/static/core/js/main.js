// random quotes
const url = 'https://quotes15.p.rapidapi.com/quotes/random/';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'e3a76ac67bmsh1fd3bab884bcbe3p110b3cjsn92ed0621ba94',
		'X-RapidAPI-Host': 'quotes15.p.rapidapi.com'
	}
};

try {
    response => response.json()
	const response = await fetch(url, options);
    fetch(options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}

