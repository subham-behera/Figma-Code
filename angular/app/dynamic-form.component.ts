import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-dynamic-form',
  templateUrl: './dynamic-form.component.html'
})
export class DynamicFormComponent implements OnInit {
  @Input() formConfig: any[] = [];
  form: FormGroup = this.fb.group({});

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    for (let field of this.formConfig) {
      if (field.type !== 'button') {
        this.form.addControl(field.key, new FormControl(''));
      }
    }
  }

  onSubmit() {
    console.log(this.form.value);
  }
}
