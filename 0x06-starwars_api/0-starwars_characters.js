#!/usr/bin/node

const request = require("request");

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  body.characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (err, res, body) => {
      const character = body.name;
      console.log(character);
    });
  });
});
