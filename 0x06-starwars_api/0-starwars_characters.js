#!/usr/bin/node

const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/';

function getCharacters (characterUrlList, index) {
  if (index === characterUrlList.length) {
    return;
  }
  request(characterUrlList[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    getCharacters(characterUrlList, index + 1);
  });
}

function printCharacters (movieId) {
  const url = BASE_URL + movieId;
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const film = JSON.parse(body);
    getCharacters(film.characters, 0);
  });
}

const movieId = process.argv[2];
printCharacters(movieId);
