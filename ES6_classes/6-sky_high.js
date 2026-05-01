import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors ;
  }

  get sqft(){
        return this._sqft;
    }
    set sqft(value){
        if (typeof value !== 'number'){
            throw new TypeError('Sqft must be a number');
        }
        this._sqft = value;
    }

    get floors(){
        return this._floors;
    }
    set floors(floors_value){
        if (typeof floors_value !== 'number'){
            throw new TypeError('Floors must be a number');
        }
        this._floors = floors_value;
    }

    evacuationWarningMessage(){
        return `Evacuate slowly the ${this._floors} floors`
    }
}