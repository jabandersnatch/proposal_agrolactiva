import { Component, OnInit } from '@angular/core';
import { NgbDateStruct, NgbCalendar } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  model: NgbDateStruct;

  docType: string;

	constructor(private calendar: NgbCalendar) {}

  ngOnInit(): void {
  }

	selectToday() {
		this.model = this.calendar.getToday();
	}

  docPicked(docPicked: string) {
    this.docType = docPicked
  }
}
