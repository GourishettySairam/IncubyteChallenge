import './App.css';
import { React, useEffect, useRef, useState } from 'react';
import axios from 'axios' ;
import Word from './Word';
// import {fetch} from 'node-fetch';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const axiosInstance = axios.create({
      baseURL: 'http://127.0.0.1:8000/'
    });

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
        <button onClick={() => {
          console.log('button clicked');
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
              <Word data={ele['fields']} />
            )
          })
        }
      </header>
    </div>
  );
}

export default App;
