export default class Airport{
    constructor(name, code){
        if (typeof name !== 'string'){
            throw new TypeError('Name must be a string');
        }
        this._name = name;

        if (typeof code !== 'string'){
            throw new TypeError('Code must be a string');
        }
        this._code = code;

    }

    get name() {
        return this._name;
    }
    set name(value){
        if (typeof value !== 'string'){
            throw new TypeError('Name must be a string');
        }
        this._name = value;
    }

    get code(){
        return this._code;
    }
    set code(code_value){
        if (typeof code_value !== 'string'){
            throw new TypeError('Code must be a string');
        }
        this._code = code_value;
    }

    get [Symbol.toStringTag]() {
        return this._code;
    }
}