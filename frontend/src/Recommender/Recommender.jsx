import './Recommender.css';
import { Card, Row, Form } from 'react-bootstrap';
import React, { useState, useEffect } from 'react';


export default class Recommender extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recommendations: [],
      searchQuery: '',
      isGame: false,
      userId: 1,
      games: [],
      movies: []
    };
  }

  handleGetRecommendationsClick = async () => {
    const data = {
      user: this.state.userId
    };

    try {
      const response = await fetch('http://192.168.1.238:5000/favorites', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
  
      const result = await response.json();
      this.setState({ games: result.games, movies: result.movies });
    } catch (error) {
      console.error(error);
    }
  };
  
  
  handleRecommendClick = async () => {
    const data = {
      [this.state.isGame ? 'game' : 'movie']: this.state.searchQuery,
      isGame: this.state.isGame, user: this.state.userId
    };

    try {
      const response = await fetch('http://192.168.1.238:5000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      this.setState({ recommendations: result.recs });
      console.log(result.recs);
    } catch (error) {
      console.error(error);
    }
  };

  handleSearchClick = () => {
    this.setState({ userId: this.state.userId, recommendations: [], searchQuery: '', isGame: false,games: [], movies: []  });
  };  

  render() {
    const { recommendations, isGame, games, movies, userId } = this.state;
    return (
      <div className="main-container">
        <div className="userId-container">
          <h4>User ID: {this.state.userId}</h4>
          <div>
            <input className="userIdSearch" type="text" value={this.state.userId} onChange={(e) => this.setState({ userId: e.target.value })} placeholder="Search user ID" />
            <button onClick={this.handleSearchClick}>Change user ID</button>
          </div>
        </div>


        <div className='title'>
          <h1>DomainHop</h1>
        </div>
        <h3 style={{ color: 'white' }}>Click below to view the recommended 8 video games and 8 movies based on your history</h3>
        <div className='search-bar' style={{ textAlign: 'center' }}>
          <div className='buttons'>
            <button onClick={this.handleGetRecommendationsClick}>Get Your Recommendations</button>
          </div>
        </div>


        <div className="App">
        {movies.length > 0 && <h2 style={{ color: 'white' }}>Top 8 Video Games</h2>}
          <Row className="mx-2 row row-cols-4">
            {games.map((rec, index) => (
              <Card key={index}>
                <Card.Img variant="top" src={rec.image} />
                <Card.Body>
                  <Card.Title>{rec}</Card.Title>
                </Card.Body>
                <Card.Footer>
                  <small className="text-muted">{rec.genre}</small>
                </Card.Footer>
              </Card>
            ))}
          </Row>
        </div>

        <div className="App">
          {movies.length > 0 && <h3 style={{ color: 'white' }}>Top 8 Movies</h3>}
          <Row className="mx-2 row row-cols-4">
            {movies.map((rec, index) => (
              <Card key={index}>
                <Card.Img variant="top" src={rec.image} />
                <Card.Body>
                  <Card.Title>{rec}</Card.Title>
                </Card.Body>
                <Card.Footer>
                  <small className="text-muted">{rec.genre}</small>
                </Card.Footer>
              </Card>
            ))}
          </Row>
        </div>
  
        <h3 style={{ color: 'white' }}>Not satisfied? Toggle the checkbox to recommend games from a movie or vice versa</h3>
        <label className="switch" style={{ color: 'white' }}>
          <input type="checkbox" checked={isGame} onChange={(e) => this.setState({ isGame: e.target.checked })} />
          <span className="slider round">{isGame ? 'Recommend games' : 'Recommend movies'}</span>
        </label>
        <br />
        <input type="text" value={this.state.searchQuery} onChange={(e) => this.setState({ searchQuery: e.target.value })} placeholder="Search..." />
  
        <div className='search-bar'>
          <div className='buttons'>
            <button onClick={this.handleRecommendClick}>Recommend</button>
            {/* <button>Get Your Recommendations</button> // added button */}
          </div>
        </div>
  
        <div className="App">
          {<h4 style={{ color: 'white' }}>Top 10 Recommendations</h4>}
          <Row className="mx-2 row row-cols-4">
            {recommendations.map((rec, index) => (
              <Card key={index}>
                <Card.Img variant="top" src={rec.image} />
                <Card.Body>
                  <Card.Title>{rec}</Card.Title>
                </Card.Body>
                <Card.Footer>
                  <small className="text-muted">{rec.genre}</small>
                </Card.Footer>
              </Card>
            ))}
          </Row>
        </div>
  
      </div>
    )
  }
  
  
}



// import './Recommender.css';
// import { Card, Row, Form } from 'react-bootstrap';
// import React, { useState, useEffect } from 'react';


// export default class Recommender extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       recommendations: [],
//       searchQuery: '',
//       isGame: false, // added boolean state
//     };
//   }

  
//   handleRecommendClick = async () => {
//     const data = {
//       [this.state.isGame ? 'game' : 'movie']: this.state.searchQuery,
//       isGame: this.state.isGame,
//     };

//     try {
//       const response = await fetch('http://192.168.1.238:5000/recommend', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//       });

//       const result = await response.json();
//       this.setState({ recommendations: result.recs });
//       console.log(result.recs);
//     } catch (error) {
//       console.error(error);
//     }
//   };


//   render() {
//     const { recommendations, isGame } = this.state;
//     return (
//       <div className="main-container">
//         <div className='title'>
//           <h1>DomainHop</h1>
//         </div>
  
//         <h3 style={{ color: 'white' }}>Toggle the Checkbox to Recommend Games from a Movie or Vice Versa</h3>
//         <label className="switch" style={{ color: 'white' }}>
//           <input type="checkbox" checked={isGame} onChange={(e) => this.setState({ isGame: e.target.checked })} />
//           <span className="slider round">{isGame ? 'Games' : 'Movies'}</span>
//         </label>
  
//         <input type="text" value={this.state.searchQuery} onChange={(e) => this.setState({ searchQuery: e.target.value })} placeholder="Search..." />
  
//         <div className='search-bar'>
//           <div className='buttons'>
//             <button onClick={this.handleRecommendClick}>Recommend</button>
//           </div>
//         </div>
  
//         <div className="App">
//           <h3 style={{ color: 'white' }}>Top 10 Recommendations</h3>
//           <Row className="mx-2 row row-cols-4">
//             {recommendations.map((rec, index) => (
//               <Card key={index}>
//                 <Card.Img variant="top" src={rec.image} />
//                 <Card.Body>
//                   <Card.Title>{rec}</Card.Title>
//                 </Card.Body>
//                 <Card.Footer>
//                   <small className="text-muted">{rec.genre}</small>
//                 </Card.Footer>
//               </Card>
//             ))}
//           </Row>
//         </div>
  
//       </div>
//     )
//   }
  
  
// }
