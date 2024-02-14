#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, async (err, res, body) => {
  if (err) {
    return console.error(err);
  }

  try {
    const characters = await Promise.all(
      body.characters.map(async (characterUrl) => {
        const characterData = await new Promise((resolve, reject) => {
          request(characterUrl, { json: true }, (err, res, body) => {
            if (err) {
              reject(err);
            } else {
              resolve(body.name);
            }
          });
        });
        return characterData;
      })
    );
    characters.forEach((character) => console.log(character));
  } catch (error) {
    console.error(error);
  }
});
