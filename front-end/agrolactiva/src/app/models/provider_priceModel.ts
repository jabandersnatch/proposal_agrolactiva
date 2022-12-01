export class ProviderPriceModel {
  id_provider: string;
  price: number;
  start_date: Date;
  end_date: Date;

  public constructor(
    id_provider: string,
    price: number,
    start_date: Date,
    end_date: Date
  ) {
    this.id_provider = id_provider;
    this.price = price;
    this.start_date = start_date;
    this.end_date = end_date;
  }
}
