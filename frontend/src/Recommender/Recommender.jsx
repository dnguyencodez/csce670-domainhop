import React from 'react';
import './Recommender.css';
import SearchBar from './SearchBar';
import { Card, Row } from 'react-bootstrap';

export default class Recommender extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            recommendations: [],
            searchQuery: ''
        };
    }
    
    handleRecommendClick = async () => {
      const data = {
          movie: this.state.searchQuery,
          isMovie: true
      };
  
      try {
          const response = await fetch("http://192.168.1.238:5000/recommendGames", {
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
        const { recommendations } = this.state;
        return (
            <div className="main-container">
                <div className='title'>
                    <h1>DomainHop</h1>
                </div>
                {/* <div className='search-bar'>
                    <div className='buttons'>
                        <SearchBar/>
                        <button onClick={() =>this.search()}>Search</button>
                    </div>
                </div> */}
                {/* <div className='search-bar'>
                    <div className='buttons'>
                        <SearchBar/>
                        <button onClick={() =>this.add()}>Add</button>
                    </div>
                </div> */}
                <input type="text" value={this.state.searchQuery} onChange={(e) => this.setState({searchQuery: e.target.value})} placeholder="Search..." />

                <div className='search-bar'>
                    <div className='buttons'>
                        {/* <SearchBar/> */}
                        <button onClick={this.handleRecommendClick}>Recommend</button>
                    </div>
                </div>

                {/* <div className='search-bar'>
                    <div className='buttons'>
                        <button onClick={this.handleRecommendClick}>Recommend</button>
                    </div>
                </div> */}
                <div className="App">
                  <Row className="mx-2 row row-cols-4">
                    {recommendations.map((rec, index) => (
                      <Card key={index}>
                        <Card.Img variant="top" src={rec.image} />
                        <Card.Body>
                          <Card.Title>{rec.title}</Card.Title>
                          <Card.Text>{rec.description}</Card.Text>
                        </Card.Body>
                        <Card.Footer>
                          <small className="text-muted">{rec.genre}</small>
                        </Card.Footer>
                      </Card>
                    ))}
                  </Row>
                </div>

                {/* <div className="App">
                    <Row className='mx-2 row row-cols-4'>
                        {recommendations.map((rec, index) => (
                            <Card key={index}>
                                <Card.Img src={rec.image}/>
                                <Card.Body>
                                    <Card.Title>
                                        {rec.title}
                                    </Card.Title>
                                </Card.Body>
                            </Card>
                        ))}
                    </Row>
                </div> */}
            </div>
        )
    }
}


// import React from 'react';
// import './Recommender.css';
// import SearchBar from './SearchBar';
// import { Card, Row } from 'react-bootstrap';

// export default class Recommender extends React.Component {

    
    
//     search() {

//     }

//     add() {

//     }

//     recommend() {

//     }

//     render() {
//         return (
//             <div className="main-container">
//                 <div className='title'>
//                     <h1>DomainHop</h1>
//                 </div>
//                 <div className='search-bar'>
//                     <div className='buttons'>
//                         <SearchBar/>
//                         <button onClick={() =>this.search()}>Search</button>
//                     </div>
//                 </div>
//                 {/* <div className='search-bar'>
//                     <div className='buttons'>
//                         <SearchBar/>
//                         <button onClick={() =>this.add()}>Add</button>
//                     </div>
//                 </div> */}
//                 <div className='search-bar'>
//                     <div className='buttons'>
//                         <button onClick={() =>this.recommend()}>Recommend</button>
//                     </div>
//                 </div>
//                 <div className="App">
//                     <Row className='mx-2 row row-cols-4'>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     <Card>
//                         <Card.Img src=""/>
//                         <Card.Body>
//                             <Card.Title>
//                                 Movie Card
//                             </Card.Title>
//                         </Card.Body>
//                     </Card>
//                     </Row>
//                 </div>
//             </div>
            
//         )
//     }
// }
