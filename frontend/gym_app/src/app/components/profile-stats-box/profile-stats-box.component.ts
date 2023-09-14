import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile-stats-box',
  template: `
    <div class="box">
      <div class="height-card">
        <div class="height-text">
          <div class="text-wrapper">{{ number }}</div>
          <div class="div">{{ label }}</div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      .box {
        width: 95px;
        height: 65px;
      }

      .box .height-card {
        position: fixed;
        width: 95px;
        height: 65px;
        top: 0;
        left: 0;
        background-color: #ffffff;
        border-radius: 16px;
        box-shadow: 0px 10px 40px #1d161712;
      }

      .box .height-text {
        position: relative;
        width: 50px;
        height: 44px;
        top: 11px;
        left: 24px;
      }

      .box .text-wrapper {
        position: absolute;
        top: 0;
        left: 0;
        background: linear-gradient(
          180deg,
          rgb(58, 106, 135) 0%,
          rgb(157, 206, 255) 100%
        );
        -webkit-background-clip: text !important;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        text-fill-color: transparent;
        font-family: 'Font Awesome 5 Free-Regular', Helvetica;
        font-weight: 400;
        color: transparent;
        font-size: 14px;
        letter-spacing: 0;
        line-height: 21px;
        white-space: nowrap;
      }

      .box .div {
        position: absolute;
        top: 26px;
        left: 3px;
        font-family: 'Font Awesome 5 Free-Regular', Helvetica;
        font-weight: 400;
        color: #7b6f72;
        font-size: 12px;
        letter-spacing: 0;
        line-height: 18px;
        white-space: nowrap;
      }
    `,
  ],
})
export class ProfileStatsBoxComponent {
  @Input() number: string = '180cm';
  @Input() label: string = 'Height';
}
