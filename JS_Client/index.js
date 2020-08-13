const request = require('request')


const client_test = () => {
request('http://localhost:3000/hello', {json:true} (err,res, body) => {
	console.log(body.url)
})
}

client_test()