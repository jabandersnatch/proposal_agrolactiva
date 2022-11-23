export class ProductDispatchModel {
  id_route: string;
  id_delivery: string;
  id_dispatched_by: string;
  id_client: string;
  dispatch_date: Date;
  quantity: number;

  public constructor(
    id_route: string,
    id_delivery: string,
    id_dispatched_by: string,
    id_client: string,
    dispatch_date: Date,
    quantity: number
  ) {
    this.id_route = id_route;
    this.id_delivery = id_delivery;
    this.id_dispatched_by = id_dispatched_by;
    this.id_client = id_client;
    this.dispatch_date = dispatch_date;
    this.quantity = quantity;
  }
}
