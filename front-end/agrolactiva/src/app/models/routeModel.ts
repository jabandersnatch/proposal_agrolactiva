import { LocationModel } from "./locationModel";

export class RouteModel {
  n_providers: number;
  avg_daily_product_income: number;
  route_type: string;
  locations: LocationModel

  public constructor(
    n_providers: number,
    avg_daily_product_income: number,
    route_type: string,
    locations: LocationModel
  ) {
    this.n_providers = n_providers;
    this.avg_daily_product_income = avg_daily_product_income;
    this.route_type = route_type;
    this.locations = locations;
  }
}
