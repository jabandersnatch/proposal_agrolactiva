export class ProductControlModel {
  id_provider: string;
  id_delivery: string;
  quantity: number;
  id_provider_price: string;
  payment_amount: number;

  public constructor(
    id_provider: string,
    id_delivery: string,
    quantity: number,
    id_provider_price: string,
    payment_amount: number
  ) {
    this.id_provider = id_provider;
    this.id_delivery = id_delivery;
    this.quantity = quantity;
    this.id_provider_price = id_provider_price;
    this.payment_amount = payment_amount;
  }
}
