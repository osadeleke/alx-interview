#!/usr/bin/node
const util = require('util');
const request = require('request');
const requestPromise = util.promisify(request);

async function fetchAndPrintCharacter (characterUrl) {
  console.log(characterUrl);
  const response = await requestPromise(characterUrl, { json: true });
  if (response.statusCode !== 200) {
    console.error(`Unexpected status code ${response.statusCode}`);
    return;
  }
  console.log(response.body.name);
}

async function processCharacterUrls (characterUrls) {
  for (const characterUrl of characterUrls) {
    await fetchAndPrintCharacter(characterUrl);
  }
}

function fetchMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  console.log(url);

  request(url, { json: true }, (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    if (res.statusCode !== 200) {
      console.error(res.statusCode);
      return;
    }

    const characterUrls = body.characters;
    processCharacterUrls(characterUrls);
  });
}

const args = process.argv.slice(2);
fetchMovieCharacters(args[0]);
