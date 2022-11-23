export class DeliveryModel {
  id_route: string;
  id_delivered_by: string;
  id_received_by: string;
  delivery_date: Date;
  quantity: number;

  public constructor(
    id_route: string,
    id_delivered_by: string,
    id_received_by: string,
    delivery_date: Date,
    quantity: number
  ) {
    this.id_route = id_route;
    this.id_delivered_by = id_delivered_by;
    this.id_received_by = id_received_by;
    this.delivery_date = delivery_date;
    this.quantity = quantity;
  }
}
