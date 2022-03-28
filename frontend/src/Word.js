import './App.css';
import { React, useEffect, useRef, useState } from 'react';
import axios from 'axios';

function Word(props) {

  const [word, setWord] = useState("");

  return (
    <>
    <div 
      key={props.data.pk} >
      <input type="text" placeholder={props.data['fields'].word} onChange={
        (e) => {
            setWord(e.target.value);
        }
      }/> &nbsp;
      <button onClick={() => {
            const axiosInstance = axios.create({
              baseURL: 'http://127.0.0.1:8000/',
            });
        
            axiosInstance.put(`/word/updateWord/${props.data.pk}/`, {word: word})
            .then(res => {
              props.setData(res.data);
            });
      }}>
        Update
      </button>&nbsp;
      <button onClick={() => {
            const axiosInstance = axios.create({
              baseURL: 'http://127.0.0.1:8000/',
            });
        
            axiosInstance.delete(`/word/deleteWord/${props.data.pk}/`)
            .then(res => {
              props.setData(res.data);
            });
      }}>
        Delete
      </button>&nbsp;
    </div>
    </>
  );
}

export default Word;
