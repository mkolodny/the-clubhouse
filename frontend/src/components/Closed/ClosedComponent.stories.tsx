import React from 'react';
import { storiesOf } from '@storybook/react';

import '../../index.css';
import Closed from '.';

storiesOf('Closed', module)
  .add('default', () => (
    <div>
      <link href="https://fonts.googleapis.com/css?family=Monoton|Lato&display=block" rel="stylesheet"></link>
      <Closed />
    </div>
  ));
