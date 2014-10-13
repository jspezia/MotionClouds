#! /bin/sh

echo 'attention: la suppression des fichiers doit se faire manuellement ā la racine de gh-pages mais aussi dans site/:
	git rm -r path/dossier/*
	git rm path/fichier'
cd ..
rm -rf assets blog categories galleries posts
mv site/output/* ./
git add .
git commit -m 'update'
git push
