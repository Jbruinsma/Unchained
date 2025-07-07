export function resolveCoverURL(cover) {
  return cover.startsWith('/uploads')
    ? `http://127.0.0.1:5000${cover}`
    : cover
}

export function displayArtist(artist) {
  return artist && artist.trim() !== "" && artist !== "null" ? artist : "";
}
