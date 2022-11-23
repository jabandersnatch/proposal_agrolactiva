import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms'
import { first } from 'rxjs/operators';
import { PersonService } from '../services/person.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  myform: FormGroup;

  error: boolean = false

  constructor(private personService: PersonService) { }

  ngOnInit() {
  }

  get f() {
    return this.myform.controls;
  }

  onSubmit(username: string, password: string) {
    this.error = false

    this.personService.login(username, password)
      .subscribe(data => {
        console.log(data)
      },
        () => {
          this.error = true
        })
  }

}
