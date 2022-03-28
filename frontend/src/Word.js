import './App.css';
import { React, useEffect, useRef, useState } from 'react';

function Word(props) {

  return (
    <div key={props.data.pk} onClick={() => {
      }}>{props.data.word}</div>
  );
}

export default Word;
