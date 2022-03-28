import './App.css';
import { React, useEffect, useRef, useState } from 'react';
import axios from 'axios' ;
import Word from './Word';
// import {fetch} from 'node-fetch';

function App() {
  const [data, setData] = useState([]);

  const [newWord, setNewWord] = useState("");

  useEffect(() => {
    const axiosInstance = axios.create({
      baseURL: 'http://127.0.0.1:8000/'
    });

    console.log(axiosInstance.defaults);

    axiosInstance.get("/word/list")
    .then(res => {
      console.log("result is ", res);
      setData(res.data);
    });
  }, []);
  
  return (
    <div className="App">
      <h2>
        List Of Words
      </h2>
      <div>
        <input type="text" onChange={(e) => {
          setNewWord(e.target.value);
        }}/> &nbsp;
        <button onClick={() => {
            const axiosInstance = axios.create({
              baseURL: 'http://127.0.0.1:8000/',
            });
        
            axiosInstance.post(`/word/createWord/`, {word: newWord} )
            .then(res => {
              setData(res.data);
            });
      }}>
          Create new word 
        </button>
        <br />
        <br></br>
      </div>
      <header className="App-header">
        {
          data?.map(ele => {
            return (
              <Word setData={setData} data={ele} />
            )
          })
        }
      </header>
    </div>
  );
}

export default App;
