#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const characterPromises = body.characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, { json: true }, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then((characters) => {
      characters.forEach((character) => {
        console.log(character);
      });
    })
    .catch((err) => {
      console.error(err);
    });
});
