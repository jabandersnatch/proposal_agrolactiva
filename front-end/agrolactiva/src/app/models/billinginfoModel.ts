export class BillingInfoModel {
  id_person: string;
  payment_type: string;
  bank: string;
  account_number: string;
  account_type: string;
  id_representative: number;

  public constructor(
    id_person: string,
    payment_type: string,
    bank: string,
    account_number: string,
    account_type: string,
    id_representative: number,
  ) {
    this.id_person = id_person;
    this.payment_type = payment_type;
    this.bank = bank;
    this.account_number = account_number;
    this.account_type = account_type;
    this.id_representative = id_representative;
  }
}
