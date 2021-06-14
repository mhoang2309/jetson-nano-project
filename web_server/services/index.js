const axios = require('axois')

const getVideo = () =>{
    const config = {
        method: 'get',
        url: 'http://localhost:5000/videos',
        headers: { }
    };
      
    axios(config)
    .then(function (response) {
    console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
    console.log(error);
    });
      
}