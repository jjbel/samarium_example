echo off

cmake --build --preset default
.\build\Release\%1.exe
