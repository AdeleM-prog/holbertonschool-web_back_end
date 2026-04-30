import Currency from "./3-currency.js";

export default class Pricing{
    constructor(amount, currency){
        if (typeof amount !== 'number'){
            throw new TypeError('Amount must be a number');
        }
        this._amount = amount;

        if (!(currency instanceof Currency)) {
            throw new TypeError('Currency must be a Currency instance');
        }
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }
    set amount(value){
        if (typeof value !== 'number'){
            throw new TypeError('Amount must be a number');
        }
        this._amount = value;
    }

    get currency(){
        return this._currency;
    }
    set currency(currency_value){
        if (!(currency_value instanceof Currency)) {
            throw new TypeError('Currency must be a Currency instance');
        }
        this._currency = currency_value;
    }

    displayFullCurrency(){
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    static convertPrice(amount, conversionRate){
        return amount * conversionRate;
    }
}