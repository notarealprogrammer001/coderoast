@echo off 
REM Script to initialize git repository 
git init 
git remote add origin https://github.com/notarealprogrammer001/coderoast 
git add . 
git commit -m "Initial commit with correct structure" 
git push -u origin main 
