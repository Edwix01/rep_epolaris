const express = require("express")
const app = express()
app.arguments(express.json())

const students = [
    {id:1,name:'Jorge',age:20,enroll:true},
    {id:2,name:'Edwin',age:24,enroll:true},
    {id:3,name:'Naty',age:25,enroll:false},
];
