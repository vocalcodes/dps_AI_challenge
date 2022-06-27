const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const jsonBody = {
  github: 'https://github.com/vocalcodes/dps_AI_challenge',
  email: 'danishmurad@gmail.com',
  url: 'https://dps-ai-challenge-danish.herokuapp.com/',
  notes: 'Repository contains all the visualizations, code, as well as the model that has been deployed on Heroku'
};

const password = hotpTotpGenerator.totp({
  key: 'danishmurad@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, jsonBody, { headers })
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));