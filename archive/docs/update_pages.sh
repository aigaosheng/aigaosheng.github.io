 bundle exec jekyll build

echo "delete files in docs"
rm -rf docs/*

echo "copy files to docs"
cp -a site_staging/* docs

echo "commit"
git add .
git commit -m "update home pages"
git push

