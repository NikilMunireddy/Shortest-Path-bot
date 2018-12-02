import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { App ,App1 } from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
ReactDOM.render(<App1 />, document.getElementById('root1'));
registerServiceWorker();
