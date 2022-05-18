#!/usr/bin/node
/**
   interacting with swapi api
   script will display challacters of a movie given movie Id
**/

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/';
request(baseUrl + 'films/' + movieId, async (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (!error) {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
