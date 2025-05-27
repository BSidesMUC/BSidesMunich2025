docker run --volume=".:/srv/jekyll" --volume=".\vendor\bundle:/usr/local/bundle" --env JEKYLL_ENV=development -p 4000:4000 -it jekyll/jekyll:3.8 jekyll serve --watch --incremental --trace
