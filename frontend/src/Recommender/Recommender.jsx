import React from 'react';
import './Recommender.css';
import { Card, Row, Form } from 'react-bootstrap';

export default class Recommender extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recommendations: [],
      searchQuery: '',
      isGame: false, // added boolean state
    };
  }

  
  handleRecommendClick = async () => {
    const data = {
      [this.state.isGame ? 'game' : 'movie']: this.state.searchQuery,
      isGame: this.state.isGame,
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


  render() {
    const { recommendations, isGame } = this.state;
    return (
      <div className="main-container">
        <div className='title'>
          <h1>DomainHop</h1>
        </div>
  
        <h3 style={{ color: 'white' }}>Toggle the Checkbox to Recommend Games from a Movie or Vice Versa</h3>
        <label className="switch" style={{ color: 'white' }}>
          <input type="checkbox" checked={isGame} onChange={(e) => this.setState({ isGame: e.target.checked })} />
          <span className="slider round">{isGame ? 'Games' : 'Movies'}</span>
        </label>
  
        <input type="text" value={this.state.searchQuery} onChange={(e) => this.setState({ searchQuery: e.target.value })} placeholder="Search..." />
  
        <div className='search-bar'>
          <div className='buttons'>
            <button onClick={this.handleRecommendClick}>Recommend</button>
          </div>
        </div>
  
        <div className="App">
          <h3 style={{ color: 'white' }}>Top 10 Recommendations</h3>
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
  
        <div className="App">
          <h3 style={{ color: 'white' }}>Five of Your Video Games</h3>
          <Row className="mx-2 row row-cols-4">
            {['Wii Sports', 'Super Mario Bros.', 'Mario Kart Wii', 'Wii Sports Resort', 'Pokemon Red/Pokemon Blue'].map((game, index) => (
              <Card key={index}>
                <Card.Body>
                  <Card.Title>{game}</Card.Title>
                </Card.Body>
              </Card>
            ))}
          </Row>
        </div>
  
        <div className="App">
          <h3 style={{ color: 'white' }}>Five of Your Movies</h3>
          <Row className="mx-2 row row-cols-4">
            {['Toy Story (1995)', 'Jumanji (1995)', 'Father of the Bride Part II (1995)', 'Heat (1995)', 'Sabrina (1995)'].map((movie, index) => (
              <Card key={index}>
                <Card.Body>
                  <Card.Title>{movie}</Card.Title>
                </Card.Body>
              </Card>
            ))}
          </Row>
        </div>
  
      </div>
    )
  }
  
  // render() {
  //   const { recommendations, isGame } = this.state;
  //   return (
  //     <div className="main-container">
  //       <div className='title'>
  //         <h1>DomainHop</h1>
  //       </div>
  
  //       <h3 style={{ color: 'white' }}>Toggle the Checkbox to Recommend Games from a Movie or Vice Versa</h3>
  //       <label className="switch" style={{ color: 'white' }}>
  //         <input type="checkbox" checked={isGame} onChange={(e) => this.setState({ isGame: e.target.checked })} />
  //         <span className="slider round">{isGame ? 'Games' : 'Movies'}</span>
  //       </label>
  
  //       <input type="text" value={this.state.searchQuery} onChange={(e) => this.setState({ searchQuery: e.target.value })} placeholder="Search..." />
  
  //       <div className='search-bar'>
  //         <div className='buttons'>
  //           <button onClick={this.handleRecommendClick}>Recommend</button>
  //         </div>
  //       </div>
  
  //       <div className="App">
  //         <h3 style={{ color: 'white' }}>Top 10 Recommendations</h3>
  //         <Row className="mx-2 row row-cols-4">
  //           {recommendations.map((rec, index) => (
  //             <Card key={index}>
  //               <Card.Img variant="top" src={rec.image} />
  //               <Card.Body>
  //                 <Card.Title>{rec}</Card.Title>
  //               </Card.Body>
  //               <Card.Footer>
  //                 <small className="text-muted">{rec.genre}</small>
  //               </Card.Footer>
  //             </Card>
  //           ))}
  //         </Row>
  //       </div>
  //     </div>
  //   )
  // }
}
