import React from 'react';
import './Recommender.css';
import SearchBar from './SearchBar';
import { Card, Row } from 'react-bootstrap';

export default class Recommender extends React.Component {

    
    
    search() {

    }

    add() {

    }

    recommend() {

    }

    render() {
        return (
            <div className="main-container">
                <div className='title'>
                    <h1>Cross-Domain Recommender</h1>
                </div>
                <div className='search-bar'>
                    <div className='buttons'>
                        <SearchBar/>
                        <button onClick={() =>this.search()}>Search</button>
                    </div>
                </div>
                <div className='search-bar'>
                    <div className='buttons'>
                        <SearchBar/>
                        <button onClick={() =>this.add()}>Add</button>
                    </div>
                </div>
                <div className='search-bar'>
                    <div className='buttons'>
                        <button onClick={() =>this.recommend()}>Recommend</button>
                    </div>
                </div>
                <div className="App">
                    <Row className='mx-2 row row-cols-4'>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    <Card>
                        <Card.Img src=""/>
                        <Card.Body>
                            <Card.Title>
                                Movie Card
                            </Card.Title>
                        </Card.Body>
                    </Card>
                    </Row>
                </div>
            </div>
            
        )
    }
}
