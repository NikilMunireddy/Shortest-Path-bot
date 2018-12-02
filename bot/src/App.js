import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
//import {axios} from 'axios';

class App1 extends Component{
  render(){
    return(
      <div>
<center>
<div class="card"><br/>

  <div class="container">

    
    
    <form action="http://localhost:5017/home" method="POST">
        <p>port:5006</p>
          <input type="text" name="src" placeholder="Source: "/>
          <br/>
          <input type="text" name="dest" placeholder="Destination: "/>
          <br/>
          <br/>
          <input class="button" type="submit" name="OK"/>
          <br/>
          <br/>
          .
      </form>
  
  
  </div>
  
</div>
</center>
     
        </div>
    );
  }
}

class App extends Component{
  
  constructor(){
    super()
    this.state={
      data:''
    }
  }
  componentDidMount() {
    //var self = this;
    
    
    fetch('http://localhost:5017/home/plot', {
    mode: 'cors',
    method: 'GET',
    
    //credentials: 'include',
    body: JSON.stringify(this.state.data),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      method:'GET',
      mode: 'cors',
    }
  }).then((response)=> {
        return response.json()
      }).then((data)=> {
        this.setState({ data:data }, () => console.log(this.state));
      }).catch((error) => {
        console.log('err')
        this.setState({data : 'error'})
      });
  }
  render() {
    return (
      <div>
      <br/><br/><br/><br/><br/><br/><br/>
      
      {this.state.data}</div>
    );
  }
  
}



export { App ,App1 };
