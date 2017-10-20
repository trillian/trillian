import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

class App extends Component {

  componentDidMount() {
    // initialise map
    var map = L.map('mapid').setView([51.505, -0.09], 13);
    // add tiles via api call
    L.TileLayer.Kitten = L.TileLayer.extend({
      getTileUrl: function(coords) {
          var i = Math.ceil( Math.random() * 4 );
          return "http://placekitten.com/256/256?image=" + i;
      }
    });
    
    L.tileLayer.kitten = function() {
        return new L.TileLayer.Kitten();
    }
    
    L.tileLayer.kitten().addTo(map);
  }

  render() {
    
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <div id="mapid"></div>
      </div>
    );
  }
}

export default App;
