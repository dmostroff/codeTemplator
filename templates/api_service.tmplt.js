import axios from "axios";

const baseUrl = 'http://'+process.env.VUE_APP_BASE_URL;
console.log( baseUrl, process.env.NODE_ENV, process.env.VUE_APP_TITLE, process.env.VUE_APP_VERSION, process.env.VUE_APP_MODE)


export default {
    getHttpRequest: (url) => {
        let fullUrl = `${baseUrl}/${url}`;
        return axios.get(fullUrl)
            .then(function (response) {
                // handle success
                return response;
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .finally(function () {
                // always executed
            });
    },

    postHttpRequest( url, formdata) {
        let fullUrl = `${baseUrl}/${url}`;
        let config = {
            headers: {
                'content-type': 'multipart/form-data'
            }
         }
        return axios.post(fullUrl, formdata, config)
            .then((response) => {
                // handle success
                return response;
            })
            .catch((error) => {
                // handle error
                console.log(error);
            })
            .finally(() => {
                // always executed
            });
    },

}